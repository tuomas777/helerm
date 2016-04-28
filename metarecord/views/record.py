from rest_framework import serializers, viewsets

from metarecord.models import Record, RecordAttachment
from .base import DetailSerializerMixin, StructuralElementSerializer


class RecordAttachmentSerializer(StructuralElementSerializer):
    class Meta(StructuralElementSerializer.Meta):
        model = RecordAttachment


class RecordAttachmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = RecordAttachment.objects.all()
    serializer_class = RecordAttachmentSerializer


class RecordListSerializer(StructuralElementSerializer):
    class Meta(StructuralElementSerializer.Meta):
        model = Record

    attachments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


class RecordDetailSerializer(StructuralElementSerializer):
    class Meta(StructuralElementSerializer.Meta):
        model = Record

    attachments = RecordAttachmentSerializer(many=True, read_only=True)


class RecordViewSet(DetailSerializerMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordListSerializer
    serializer_class_detail = RecordDetailSerializer